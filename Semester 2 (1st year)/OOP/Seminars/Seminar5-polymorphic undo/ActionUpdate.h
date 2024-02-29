#pragma once
#include "Action.h"
class ActionUpdate :
    public Action
{
private:
    Song previousSong;
    Song newSong;
    Repository& repo;
public:
    ActionUpdate(Repository& repo, Song prevSong, Song newSong): repo{repo}, previousSong{prevSong}, newSong{newSong}{}
    void executeUndo() override;
    void executeRedo() override;
};

