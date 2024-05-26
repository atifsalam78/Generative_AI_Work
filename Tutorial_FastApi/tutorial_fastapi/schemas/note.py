def noteEntity(item) -> dict:
    return {
        "note_id" : str(item["note_id"]),
        "title" : item["title"],
        "desc" : item["desc"],
        "important" : item["important"]
    }

def notesEntity(items) -> list:
    return [noteEntity(item) for item in items]