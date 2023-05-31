from teacher_crud import TeacherCRUD
from cli import TeacherCLI

teacherCRUD = TeacherCRUD()

cli = TeacherCLI(teacherCRUD)
cli.run()
