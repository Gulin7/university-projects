#pragma once
#include "Action.h"
#include "Repository.h"
#include "Song.h"
#include "PlayList.h"

class ActionRemove :
    public Action
{
private:
    Song removedSong;
    Repository& repo;
public:
    ActionRemove(Repository& repo, Song song): repo{repo}, removedSong{song}{}
    void executeUndo() override;
    void executeRedo() override;
};

