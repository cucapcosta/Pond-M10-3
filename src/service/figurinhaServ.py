from repository.figurinhaRepo import FigurinhaRepository
class FigurinhaService():
    def addFig(fig):
        return FigurinhaRepository().save(fig)
    def getAllFigs():
        return FigurinhaRepository().getAll()
    def getFigs(id: int): 
        return FigurinhaRepository().getById(id)
    def updateFig(id: int, fig):
        return FigurinhaRepository().update(id, fig)     
    def deleteFig(id: int):
        return FigurinhaRepository().delete(id)
       
       
