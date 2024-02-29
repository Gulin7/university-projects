#include "ActionRemove.h"

void ActionRemove::executeUndo()
{
	this->repo.addSong(this->removedSong);
}

void ActionRemove::executeRedo()
{
	this->repo.removeSong(this->removedSong);
}
