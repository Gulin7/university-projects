#include "Answer.h"

Answer::Answer(int id, int questionId, int numberOfVotes, string userName, string answerText) :
    id{ id }, questionId{ questionId }, numberOfVotes{ numberOfVotes }, userName{ userName }, answerText{ answerText }
{
}

int Answer::getId()
{
    return this->id;
}

int Answer::getQuestionId()
{
    return this->questionId;
}

int Answer::getNumberOfVotes()
{
    return this->numberOfVotes;
}

string Answer::getUserName()
{
    return this->userName;
}

string Answer::getAnswerText()
{
    return this->answerText;
}

void Answer::setNumberOfVotes(int newNumberOfVotes)
{
    this->numberOfVotes = newNumberOfVotes;
}

string Answer::toString()
{
    return std::to_string(this->id) + " | " + this->userName + " | " 
        + this->answerText + " | " + std::to_string(this->numberOfVotes);
}
