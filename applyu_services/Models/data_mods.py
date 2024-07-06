from typing import List

from sqlalchemy import Column, Date, DateTime, Enum, ForeignKeyConstraint, Index, String, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT, VARCHAR
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship
from sqlalchemy.orm.base import Mapped

Base = declarative_base()


class AccountType(Base):
    __tablename__ = 'account_type'

    account_type_id = mapped_column(TINYINT(4), primary_key=True, comment='PK')
    type_name = mapped_column(String(10), nullable=False, server_default=text("'original'"))

    user_account: Mapped[List['UserAccount']] = relationship('UserAccount', uselist=True, back_populates='account_type')


class StudentProgramList(Base):
    __tablename__ = 'student_program_list'

    major_id = mapped_column(String(128), primary_key=True, comment='PK')

    student_ai_reports: Mapped[List['StudentAiReports']] = relationship('StudentAiReports', uselist=True, back_populates='major')


class Tutor(Base):
    __tablename__ = 'tutor'

    tutor_id = mapped_column(String(30), primary_key=True, comment='PK')
    create_time = mapped_column(DateTime, nullable=False, server_default=text('current_timestamp()'))


class UserRegisterMethod(Base):
    __tablename__ = 'user_register_method'

    reg_mode_id = mapped_column(TINYINT(4), primary_key=True, comment='PK')
    reg_mode_name = mapped_column(String(10), nullable=False)

    user_account: Mapped[List['UserAccount']] = relationship('UserAccount', uselist=True, back_populates='reg_mode')


class UserAccount(Base):
    __tablename__ = 'user_account'
    __table_args__ = (
        ForeignKeyConstraint(['account_type_id'], ['account_type.account_type_id'], onupdate='CASCADE', name='user_account_ibfk_1'),
        ForeignKeyConstraint(['reg_mode_id'], ['user_register_method.reg_mode_id'], onupdate='CASCADE', name='user_account_ibfk_2'),
        Index('account_type_id', 'account_type_id'),
        Index('reg_mode_id', 'reg_mode_id')
    )

    user_name = mapped_column(String(30), primary_key=True, comment='PK')
    password = mapped_column(VARCHAR(30), nullable=False)
    account_type_id = mapped_column(TINYINT(4), nullable=False, comment='FK')
    reg_mode_id = mapped_column(TINYINT(4), nullable=False, comment='FK')
    country_code = mapped_column(String(3), nullable=False)
    phone = mapped_column(String(15), nullable=False)
    email = mapped_column(String(50), nullable=False)
    register_time = mapped_column(DateTime, nullable=False, server_default=text('current_timestamp()'))

    account_type: Mapped['AccountType'] = relationship('AccountType', back_populates='user_account')
    reg_mode: Mapped['UserRegisterMethod'] = relationship('UserRegisterMethod', back_populates='user_account')


class AccountActivation(UserAccount):
    __tablename__ = 'account_activation'
    __table_args__ = (
        ForeignKeyConstraint(['user_name'], ['user_account.user_name'], onupdate='CASCADE', name='account_activation_ibfk_1'),
    )

    user_name = mapped_column(String(30), primary_key=True, comment='PK,FK')
    activate_status = mapped_column(TINYINT(1), nullable=False)
    activate_time = mapped_column(DateTime)

    career_cv: Mapped[List['CareerCv']] = relationship('CareerCv', uselist=True, back_populates='account_activation')
    student_cv: Mapped[List['StudentCv']] = relationship('StudentCv', uselist=True, back_populates='account_activation')
    student_ai_reports: Mapped[List['StudentAiReports']] = relationship('StudentAiReports', uselist=True, back_populates='account_activation')


class CareerCv(Base):
    __tablename__ = 'career_cv'
    __table_args__ = (
        ForeignKeyConstraint(['user_name'], ['account_activation.user_name'], onupdate='CASCADE', name='career_cv_ibfk_1'),
        Index('user_name', 'user_name')
    )

    cv_id = mapped_column(String(42), primary_key=True, comment='PK')
    user_name = mapped_column(String(30), nullable=False, comment='FK')
    cv_path = mapped_column(String(50), nullable=False)
    create_time = mapped_column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    update_time = mapped_column(DateTime, nullable=False)

    account_activation: Mapped['AccountActivation'] = relationship('AccountActivation', back_populates='career_cv')


class StudentCv(Base):
    __tablename__ = 'student_cv'
    __table_args__ = (
        ForeignKeyConstraint(['user_name'], ['account_activation.user_name'], onupdate='CASCADE', name='student_cv_ibfk_1'),
        Index('user_name', 'user_name')
    )

    cv_id = mapped_column(String(42), primary_key=True, comment='PK')
    user_name = mapped_column(String(30), nullable=False, comment='FK')
    cv_path = mapped_column(String(50), nullable=False)
    create_time = mapped_column(DateTime, nullable=False, server_default=text('current_timestamp()'))
    update_time = mapped_column(DateTime)

    account_activation: Mapped['AccountActivation'] = relationship('AccountActivation', back_populates='student_cv')
    student_ai_reports: Mapped[List['StudentAiReports']] = relationship('StudentAiReports', uselist=True, back_populates='cv')


class UserLoginInfo(AccountActivation):
    __tablename__ = 'user_login_info'
    __table_args__ = (
        ForeignKeyConstraint(['user_name'], ['account_activation.user_name'], onupdate='CASCADE', name='user_login_info_ibfk_1'),
    )

    user_name = mapped_column(String(30), primary_key=True, comment='PK,FK')
    device = mapped_column(String(8), nullable=False)
    system = mapped_column(String(8), nullable=False)
    login_ip = mapped_column(String(15), nullable=False)
    login_time = mapped_column(DateTime, nullable=False, server_default=text('current_timestamp()'))


class UserProfile(AccountActivation):
    __tablename__ = 'user_profile'
    __table_args__ = (
        ForeignKeyConstraint(['user_name'], ['account_activation.user_name'], onupdate='CASCADE', name='user_profile_ibfk_1'),
    )

    user_name = mapped_column(String(30), primary_key=True, comment='PK,FK')
    gender = mapped_column(Enum('m', 'f'), nullable=False, server_default=text("'f'"))
    first_name = mapped_column(String(128))
    last_name = mapped_column(String(128))
    birth = mapped_column(Date)
    avatar_path = mapped_column(String(50))


class StudentAiReports(Base):
    __tablename__ = 'student_ai_reports'
    __table_args__ = (
        ForeignKeyConstraint(['cv_id'], ['student_cv.cv_id'], onupdate='CASCADE', name='student_ai_reports_ibfk_4'),
        ForeignKeyConstraint(['major_id'], ['student_program_list.major_id'], onupdate='CASCADE', name='student_ai_reports_ibfk_3'),
        ForeignKeyConstraint(['user_name'], ['account_activation.user_name'], onupdate='CASCADE', name='student_ai_reports_ibfk_1'),
        Index('cv_id', 'cv_id'),
        Index('major_id', 'major_id'),
        Index('user_name', 'user_name')
    )

    apply_id = mapped_column(INTEGER(11), primary_key=True, comment='PK')
    user_name = mapped_column(String(30), nullable=False, comment='FK')
    cv_id = mapped_column(String(42), nullable=False, comment='FK')
    major_id = mapped_column(String(128), nullable=False, comment='FK')
    applied_time = mapped_column(DateTime, nullable=False, server_default=text('current_timestamp()'))

    cv: Mapped['StudentCv'] = relationship('StudentCv', back_populates='student_ai_reports')
    major: Mapped['StudentProgramList'] = relationship('StudentProgramList', back_populates='student_ai_reports')
    account_activation: Mapped['AccountActivation'] = relationship('AccountActivation', back_populates='student_ai_reports')

