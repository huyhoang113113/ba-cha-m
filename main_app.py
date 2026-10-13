"""Composition root for the layered quiz application."""

from quiz_app.application.quiz_service import QuizService
from quiz_app.infrastructure.opentdb_question_repository import OpenTDBQuestionRepository
from quiz_app.infrastructure.paths import resource_path
from quiz_app.infrastructure.sound_manager import SoundManager
from quiz_app.infrastructure.sqlite_question_repository import SQLiteQuestionRepository
from quiz_app.presentation.quiz_window import QuizWindow


def main() -> None:
    local_questions = SQLiteQuestionRepository(resource_path("brain_quest.db"))
    api_questions = OpenTDBQuestionRepository()
    quiz_service = QuizService(local_questions, api_questions)
    app = QuizWindow(quiz_service, SoundManager())
    app.mainloop()


if __name__ == "__main__":
    main()