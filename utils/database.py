"""
Database operations for LearnPath AI
Handles SQLite database for storing learning paths and progress tracking
"""

import sqlite3
import json
from datetime import datetime
from typing import List, Dict, Optional


class Database:
    def __init__(self, db_path: str = "learnpath.db"):
        """Initialize database connection and create tables if they don't exist"""
        self.db_path = db_path
        self.init_database()

    def get_connection(self):
        """Get a database connection"""
        return sqlite3.connect(self.db_path)

    def init_database(self):
        """Create tables if they don't exist"""
        conn = self.get_connection()
        cursor = conn.cursor()

        # Learning Paths table (now supports all goal types)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS learning_paths (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                goal TEXT NOT NULL,
                timeframe INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                is_active BOOLEAN DEFAULT 1,
                status TEXT DEFAULT 'active',
                goal_type TEXT DEFAULT 'learning',
                start_date DATE,
                hours_per_day REAL DEFAULT 2.0,
                unavailable_dates TEXT,
                weekly_pattern TEXT
            )
        """)

        # Add new columns to existing tables if they don't exist
        try:
            cursor.execute("ALTER TABLE learning_paths ADD COLUMN status TEXT DEFAULT 'active'")
        except sqlite3.OperationalError:
            pass

        try:
            cursor.execute("ALTER TABLE learning_paths ADD COLUMN goal_type TEXT DEFAULT 'learning'")
        except sqlite3.OperationalError:
            pass

        # Add new date/time planning columns
        try:
            cursor.execute("ALTER TABLE learning_paths ADD COLUMN start_date DATE")
        except sqlite3.OperationalError:
            pass

        try:
            cursor.execute("ALTER TABLE learning_paths ADD COLUMN hours_per_day REAL DEFAULT 2.0")
        except sqlite3.OperationalError:
            pass

        try:
            cursor.execute("ALTER TABLE learning_paths ADD COLUMN unavailable_dates TEXT")
        except sqlite3.OperationalError:
            pass

        try:
            cursor.execute("ALTER TABLE learning_paths ADD COLUMN weekly_pattern TEXT")
        except sqlite3.OperationalError:
            pass

        # Topics table (now with priority, due dates, and notes)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS topics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                path_id INTEGER NOT NULL,
                day_number INTEGER NOT NULL,
                topic_name TEXT NOT NULL,
                subtopics TEXT,
                estimated_hours REAL,
                resources TEXT,
                is_completed BOOLEAN DEFAULT 0,
                completed_at TIMESTAMP,
                time_spent_minutes INTEGER DEFAULT 0,
                priority TEXT DEFAULT 'medium',
                due_date DATE,
                notes TEXT,
                FOREIGN KEY (path_id) REFERENCES learning_paths(id)
            )
        """)

        # Add new columns to topics table
        try:
            cursor.execute("ALTER TABLE topics ADD COLUMN priority TEXT DEFAULT 'medium'")
        except sqlite3.OperationalError:
            pass

        try:
            cursor.execute("ALTER TABLE topics ADD COLUMN due_date DATE")
        except sqlite3.OperationalError:
            pass

        try:
            cursor.execute("ALTER TABLE topics ADD COLUMN notes TEXT")
        except sqlite3.OperationalError:
            pass

        # Progress tracking table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS progress_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                path_id INTEGER NOT NULL,
                topic_id INTEGER NOT NULL,
                action TEXT NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                notes TEXT,
                FOREIGN KEY (path_id) REFERENCES learning_paths(id),
                FOREIGN KEY (topic_id) REFERENCES topics(id)
            )
        """)

        conn.commit()
        conn.close()

    def save_learning_path(self, goal: str, timeframe: int, goal_type: str = 'learning',
                          start_date: str = None, hours_per_day: float = 2.0,
                          unavailable_dates: str = None, weekly_pattern: str = None) -> int:
        """Save a new goal plan and return its ID"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO learning_paths (goal, timeframe, goal_type, start_date, hours_per_day,
                                       unavailable_dates, weekly_pattern)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (goal, timeframe, goal_type, start_date, hours_per_day, unavailable_dates, weekly_pattern))

        path_id = cursor.lastrowid
        conn.commit()
        conn.close()

        return path_id

    def save_topics(self, path_id: int, topics: List[Dict]):
        """Save action items/milestones for a goal plan"""
        conn = self.get_connection()
        cursor = conn.cursor()

        for topic in topics:
            cursor.execute("""
                INSERT INTO topics (
                    path_id, day_number, topic_name, subtopics,
                    estimated_hours, resources, priority, due_date, notes
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                path_id,
                topic.get('day', 0),
                topic.get('topic', ''),
                json.dumps(topic.get('subtopics', [])),
                topic.get('estimated_hours', 0),
                json.dumps(topic.get('resources', [])),
                topic.get('priority', 'medium'),
                topic.get('due_date', None),
                topic.get('notes', '')
            ))

        conn.commit()
        conn.close()

    def get_learning_paths(self, active_only: bool = True) -> List[Dict]:
        """Get all learning paths"""
        conn = self.get_connection()
        cursor = conn.cursor()

        if active_only:
            cursor.execute("""
                SELECT id, goal, timeframe, created_at, updated_at, status, goal_type,
                       start_date, hours_per_day, unavailable_dates, weekly_pattern
                FROM learning_paths
                WHERE is_active = 1
                ORDER BY created_at DESC
            """)
        else:
            cursor.execute("""
                SELECT id, goal, timeframe, created_at, updated_at, status, goal_type,
                       start_date, hours_per_day, unavailable_dates, weekly_pattern
                FROM learning_paths
                ORDER BY created_at DESC
            """)

        paths = []
        for row in cursor.fetchall():
            paths.append({
                'id': row[0],
                'goal': row[1],
                'timeframe': row[2],
                'created_at': row[3],
                'updated_at': row[4],
                'status': row[5] if len(row) > 5 else 'active',
                'goal_type': row[6] if len(row) > 6 else 'learning',
                'start_date': row[7] if len(row) > 7 else None,
                'hours_per_day': row[8] if len(row) > 8 else 2.0,
                'unavailable_dates': row[9] if len(row) > 9 else None,
                'weekly_pattern': row[10] if len(row) > 10 else None
            })

        conn.close()
        return paths

    def get_topics(self, path_id: int) -> List[Dict]:
        """Get all topics for a learning path"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, day_number, topic_name, subtopics, estimated_hours,
                   resources, is_completed, completed_at, time_spent_minutes,
                   priority, due_date, notes
            FROM topics
            WHERE path_id = ?
            ORDER BY day_number
        """, (path_id,))

        topics = []
        for row in cursor.fetchall():
            topics.append({
                'id': row[0],
                'day': row[1],
                'topic': row[2],
                'subtopics': json.loads(row[3]) if row[3] else [],
                'estimated_hours': row[4],
                'resources': json.loads(row[5]) if row[5] else [],
                'is_completed': bool(row[6]),
                'completed_at': row[7],
                'time_spent_minutes': row[8],
                'priority': row[9] if len(row) > 9 else 'medium',
                'due_date': row[10] if len(row) > 10 else None,
                'notes': row[11] if len(row) > 11 else ''
            })

        conn.close()
        return topics

    def update_topic_completion(self, topic_id: int, is_completed: bool, time_spent: int = 0):
        """Update topic completion status"""
        conn = self.get_connection()
        cursor = conn.cursor()

        if is_completed:
            cursor.execute("""
                UPDATE topics
                SET is_completed = 1,
                    completed_at = CURRENT_TIMESTAMP,
                    time_spent_minutes = time_spent_minutes + ?
                WHERE id = ?
            """, (time_spent, topic_id))
        else:
            cursor.execute("""
                UPDATE topics
                SET is_completed = 0,
                    completed_at = NULL,
                    time_spent_minutes = time_spent_minutes + ?
                WHERE id = ?
            """, (time_spent, topic_id))

        conn.commit()
        conn.close()

    def get_progress_stats(self, path_id: int) -> Dict:
        """Get progress statistics for a learning path"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                COUNT(*) as total_topics,
                SUM(CASE WHEN is_completed = 1 THEN 1 ELSE 0 END) as completed_topics,
                SUM(time_spent_minutes) as total_time_spent
            FROM topics
            WHERE path_id = ?
        """, (path_id,))

        row = cursor.fetchone()

        total = row[0] or 0
        completed = row[1] or 0
        time_spent = row[2] or 0

        stats = {
            'total_topics': total,
            'completed_topics': completed,
            'progress_percentage': (completed / total * 100) if total > 0 else 0,
            'total_time_spent_minutes': time_spent,
            'total_time_spent_hours': round(time_spent / 60, 1)
        }

        conn.close()
        return stats

    def log_progress(self, path_id: int, topic_id: int, action: str, notes: str = ""):
        """Log a progress action"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO progress_log (path_id, topic_id, action, notes)
            VALUES (?, ?, ?, ?)
        """, (path_id, topic_id, action, notes))

        conn.commit()
        conn.close()

    def delete_learning_path(self, path_id: int):
        """Soft delete a learning path"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE learning_paths
            SET is_active = 0, status = 'deleted'
            WHERE id = ?
        """, (path_id,))

        conn.commit()
        conn.close()

    def update_path_status(self, path_id: int, status: str):
        """
        Update the status of a learning path
        Status can be: 'active', 'on_hold', 'archived', 'deleted'
        """
        conn = self.get_connection()
        cursor = conn.cursor()

        is_active = 1 if status in ['active', 'on_hold'] else 0

        cursor.execute("""
            UPDATE learning_paths
            SET status = ?, is_active = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (status, is_active, path_id))

        conn.commit()
        conn.close()

    def get_paths_by_status(self, status: str = None) -> List[Dict]:
        """
        Get learning paths filtered by status
        If status is None, return all paths
        """
        conn = self.get_connection()
        cursor = conn.cursor()

        if status:
            cursor.execute("""
                SELECT id, goal, timeframe, created_at, updated_at, status
                FROM learning_paths
                WHERE status = ?
                ORDER BY updated_at DESC
            """, (status,))
        else:
            cursor.execute("""
                SELECT id, goal, timeframe, created_at, updated_at, status
                FROM learning_paths
                ORDER BY updated_at DESC
            """)

        paths = []
        for row in cursor.fetchall():
            paths.append({
                'id': row[0],
                'goal': row[1],
                'timeframe': row[2],
                'created_at': row[3],
                'updated_at': row[4],
                'status': row[5] if len(row) > 5 else 'active'
            })

        conn.close()
        return paths

    def update_topic_due_date(self, topic_id: int, due_date: str):
        """Update the due date for a specific topic"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE topics
            SET due_date = ?
            WHERE id = ?
        """, (due_date, topic_id))

        conn.commit()
        conn.close()

    def update_path_schedule(self, path_id: int, start_date: str = None,
                           hours_per_day: float = None, unavailable_dates: str = None,
                           weekly_pattern: str = None):
        """Update the scheduling parameters for a learning path"""
        conn = self.get_connection()
        cursor = conn.cursor()

        updates = []
        params = []

        if start_date is not None:
            updates.append("start_date = ?")
            params.append(start_date)

        if hours_per_day is not None:
            updates.append("hours_per_day = ?")
            params.append(hours_per_day)

        if unavailable_dates is not None:
            updates.append("unavailable_dates = ?")
            params.append(unavailable_dates)

        if weekly_pattern is not None:
            updates.append("weekly_pattern = ?")
            params.append(weekly_pattern)

        if updates:
            updates.append("updated_at = CURRENT_TIMESTAMP")
            params.append(path_id)

            query = f"""
                UPDATE learning_paths
                SET {', '.join(updates)}
                WHERE id = ?
            """

            cursor.execute(query, params)
            conn.commit()

        conn.close()

    def get_path_details(self, path_id: int) -> Optional[Dict]:
        """Get detailed information about a specific learning path"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, goal, timeframe, created_at, updated_at, status, goal_type,
                   start_date, hours_per_day, unavailable_dates, weekly_pattern
            FROM learning_paths
            WHERE id = ?
        """, (path_id,))

        row = cursor.fetchone()
        conn.close()

        if row:
            return {
                'id': row[0],
                'goal': row[1],
                'timeframe': row[2],
                'created_at': row[3],
                'updated_at': row[4],
                'status': row[5] if len(row) > 5 else 'active',
                'goal_type': row[6] if len(row) > 6 else 'learning',
                'start_date': row[7] if len(row) > 7 else None,
                'hours_per_day': row[8] if len(row) > 8 else 2.0,
                'unavailable_dates': row[9] if len(row) > 9 else None,
                'weekly_pattern': row[10] if len(row) > 10 else None
            }
        return None
