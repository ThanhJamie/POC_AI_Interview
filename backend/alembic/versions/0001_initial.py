"""initial schema

Revision ID: 0001_initial
Revises:
Create Date: 2026-04-06 14:50:00

"""

from __future__ import annotations

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "0001_initial"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')
    op.execute("CREATE EXTENSION IF NOT EXISTS vector")

    op.create_table(
        "interviews",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("candidate_name", sa.String(length=255), nullable=False),
        sa.Column("job_title", sa.String(length=255), nullable=True),
        sa.Column("status", sa.String(length=50), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_interviews_id"), "interviews", ["id"], unique=False)
    op.create_index(
        op.f("ix_interviews_candidate_name"),
        "interviews",
        ["candidate_name"],
        unique=False,
    )

    op.create_table(
        "messages",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("interview_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("role", sa.String(length=32), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["interview_id"], ["interviews.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_messages_id"), "messages", ["id"], unique=False)
    op.create_index(op.f("ix_messages_interview_id"), "messages", ["interview_id"], unique=False)

    op.create_table(
        "embeddings",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("interview_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("source_type", sa.String(length=64), nullable=False),
        sa.Column("source_ref", sa.String(length=255), nullable=False),
        sa.Column("vector", sa.JSON(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["interview_id"], ["interviews.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_embeddings_id"), "embeddings", ["id"], unique=False)
    op.create_index(
        op.f("ix_embeddings_interview_id"),
        "embeddings",
        ["interview_id"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index(op.f("ix_embeddings_interview_id"), table_name="embeddings")
    op.drop_index(op.f("ix_embeddings_id"), table_name="embeddings")
    op.drop_table("embeddings")

    op.drop_index(op.f("ix_messages_interview_id"), table_name="messages")
    op.drop_index(op.f("ix_messages_id"), table_name="messages")
    op.drop_table("messages")

    op.drop_index(op.f("ix_interviews_candidate_name"), table_name="interviews")
    op.drop_index(op.f("ix_interviews_id"), table_name="interviews")
    op.drop_table("interviews")
