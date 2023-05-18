#pragma once
#include "Action.h"
#include "Repository.h"
#include "Song.h"
#include "PlayList.h"

class ActionAdd :
    public Action
{
private:
    Song addedSong;
    Repository& repo;
public:
    ActionAdd(Repository& initialRepository, Song initialSong) : repo{initialRepository}, addedSong { initialSong } {}
    void executeUndo() override;
    void executeRedo() override;
};

