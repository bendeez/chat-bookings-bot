"""changed business id to account id in facility table so all accounts can create facilities for their use

Revision ID: f6c3fc51214d
Revises:
Create Date: 2024-08-23 15:16:52.368849

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f6c3fc51214d"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "accounts",
        sa.Column("type", sa.String(length=45), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "chat_messenger",
        sa.Column("type", sa.String(length=45), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "data_categories",
        sa.Column("name", sa.String(length=45), nullable=False),
        sa.Column("keywords", sa.String(length=45), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "business",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(length=45), nullable=False),
        sa.Column("email_verified", sa.Boolean(), nullable=False),
        sa.Column("subscription_id", sa.Integer(), nullable=False),
        sa.Column("location", sa.String(length=45), nullable=False),
        sa.Column("password", sa.String(length=500), nullable=False),
        sa.ForeignKeyConstraint(
            ["id"],
            ["accounts.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    op.create_table(
        "chat_agent",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["id"],
            ["chat_messenger.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "chat_sessions",
        sa.Column("id", sa.String(length=45), nullable=False),
        sa.Column("account_id", sa.Integer(), nullable=True),
        sa.Column("start_time", sa.DateTime(), nullable=False),
        sa.Column("end_time", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["account_id"],
            ["accounts.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "chat_user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("ip_address", sa.String(length=45), nullable=False),
        sa.Column("user_agent", sa.String(length=45), nullable=False),
        sa.ForeignKeyConstraint(
            ["id"],
            ["chat_messenger.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "facility",
        sa.Column("title", sa.String(length=100), nullable=False),
        sa.Column("description", sa.String(length=10000), nullable=False),
        sa.Column("account_id", sa.Integer(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["account_id"],
            ["accounts.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(length=45), nullable=False),
        sa.Column("email_verified", sa.Boolean(), nullable=False),
        sa.Column("password", sa.String(length=500), nullable=False),
        sa.ForeignKeyConstraint(
            ["id"],
            ["accounts.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    op.create_table(
        "business_data",
        sa.Column("business_id", sa.Integer(), nullable=False),
        sa.Column("category_id", sa.Integer(), nullable=False),
        sa.Column("data", sa.Text(), nullable=False),
        sa.Column("keywords", sa.String(length=45), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["business_id"],
            ["business.id"],
        ),
        sa.ForeignKeyConstraint(
            ["category_id"],
            ["data_categories.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "business_users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(length=45), nullable=False),
        sa.Column("password", sa.String(length=500), nullable=False),
        sa.Column("business_id", sa.Integer(), nullable=False),
        sa.Column("role_name", sa.String(length=45), nullable=False),
        sa.ForeignKeyConstraint(
            ["business_id"],
            ["business.id"],
        ),
        sa.ForeignKeyConstraint(
            ["id"],
            ["accounts.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    op.create_table(
        "chat_messages",
        sa.Column("session_id", sa.String(length=45), nullable=False),
        sa.Column("message", sa.Text(), nullable=False),
        sa.Column("messenger_id", sa.Integer(), nullable=False),
        sa.Column("date", sa.DateTime(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["messenger_id"],
            ["chat_messenger.id"],
        ),
        sa.ForeignKeyConstraint(
            ["session_id"],
            ["chat_sessions.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("chat_messages")
    op.drop_table("business_users")
    op.drop_table("business_data")
    op.drop_table("users")
    op.drop_table("facility")
    op.drop_table("chat_user")
    op.drop_table("chat_sessions")
    op.drop_table("chat_agent")
    op.drop_table("business")
    op.drop_table("data_categories")
    op.drop_table("chat_messenger")
    op.drop_table("accounts")
    # ### end Alembic commands ###
