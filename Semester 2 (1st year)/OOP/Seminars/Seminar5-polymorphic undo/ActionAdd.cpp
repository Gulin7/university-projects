#include "ActionAdd.h"

void ActionAdd::executeUndo()
{
	this->repo.removeSong(this->addedSong);
}

void ActionAdd::executeRedo()
{
	this->repo.addSong(this->addedSong);
}
