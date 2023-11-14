"""empty message

Revision ID: c0ab1c61729a
Revises: 
Create Date: 2023-11-14 14:21:05.830186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0ab1c61729a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Usuarios',
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('username', sa.String(length=120), nullable=False),
    sa.Column('nome', sa.String(length=120), nullable=False),
    sa.Column('senha', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('email'),
    sa.UniqueConstraint('nome'),
    sa.UniqueConstraint('username')
    )
    op.create_table('Mesas',
    sa.Column('nome_mesa', sa.String(length=120), nullable=False),
    sa.Column('id_mesa', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('mestre_email', sa.String(length=120), nullable=False),
    sa.ForeignKeyConstraint(['mestre_email'], ['Usuarios.email'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id_mesa')
    )
    op.create_table('Fichas',
    sa.Column('id_ficha', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=120), nullable=False),
    sa.Column('arquetipo', sa.String(length=120), nullable=False),
    sa.Column('xp', sa.Integer(), nullable=False),
    sa.Column('poder', sa.Integer(), nullable=False),
    sa.Column('habilidade', sa.Integer(), nullable=False),
    sa.Column('resistencia', sa.Integer(), nullable=False),
    sa.Column('tipo_ficha', sa.String(length=120), nullable=False),
    sa.Column('email_usuario', sa.String(length=120), nullable=False),
    sa.Column('id_mesa', sa.Integer(), nullable=False),
    sa.Column('id_veiculo', sa.Integer(), nullable=True),
    sa.CheckConstraint('tipo_ficha IN ("Player", "Veiculo")', name='check_tipo_ficha'),
    sa.ForeignKeyConstraint(['email_usuario'], ['Usuarios.email'], ),
    sa.ForeignKeyConstraint(['id_mesa'], ['Mesas.id_mesa'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['id_veiculo'], ['Fichas.id_ficha'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id_ficha')
    )
    op.create_table('Desvantagens',
    sa.Column('nome_desvant', sa.String(length=120), nullable=False),
    sa.Column('id_ficha', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_ficha'], ['Fichas.id_ficha'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('nome_desvant')
    )
    op.create_table('Pericias',
    sa.Column('nome_pericia', sa.String(length=120), nullable=False),
    sa.Column('id_ficha', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_ficha'], ['Fichas.id_ficha'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('nome_pericia')
    )
    op.create_table('Vantagens',
    sa.Column('nome_vant', sa.String(length=120), nullable=False),
    sa.Column('id_ficha', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_ficha'], ['Fichas.id_ficha'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('nome_vant')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Vantagens')
    op.drop_table('Pericias')
    op.drop_table('Desvantagens')
    op.drop_table('Fichas')
    op.drop_table('Mesas')
    op.drop_table('Usuarios')
    # ### end Alembic commands ###