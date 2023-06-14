#include "Testing.h"
#include <cassert>

void Testing::testAddQuestion()
{
	ParticipantsRepository participantsRepo{ "participants.txt" };
	QuestionsRepository questionsRepo{ "questionsTest.txt" };
	Service testService{ participantsRepo, questionsRepo };

	Question q1{ 1, "Ce faci?", "Bine", 2 };

	testService.addQuestion(1, "Ce faci?", "Bine", 2);

	assert(testService.getAllQuestionsSortedById()[0].getId() == 1);
	assert(testService.getAllQuestionsSortedById()[0].getText() == "Ce faci?");

	assert(questionsRepo.getAll().size() == 1);

	try 
	{
		questionsRepo.add(q1);
		assert(false);
	}
	catch (std::exception& e)
	{
		assert(true);
	}
}

void Testing::testUpdateParticipantScore()
{
	ParticipantsRepository participantsRepo{ "participants.txt" };
	QuestionsRepository questionsRepo{ "questionsTest.txt" };
	Service testService{ participantsRepo, questionsRepo };

	testService.updateParticipantScore("John", 20);
	
	int position = participantsRepo.findByName("John");

	assert(participantsRepo.getAll()[position].getScore() == 20);

	try
	{
		testService.updateParticipantScore("asdnas", 30);
		assert(false);
	}
	catch (std::exception& e)
	{
		assert(true);
	}
}

void Testing::testAll()
{
	testAddQuestion();
	testUpdateParticipantScore();
}
