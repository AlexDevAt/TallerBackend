from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from fastapi.responses import JSONResponse

class Usuario(BaseModel):
    id:int
    nombre:str
    email:str
    contra:str
    edad:int = Field(ge=0)
    
usuarios:list[Usuario] = []
idActual = 0
app = FastAPI()

@app.get("/")
async def primerEndpoint():
    return {
        "hola":"mundo"
    }
    
@app.get("/usuarios/{id}")
async def obtenerUsuario(id:int):
    return{
        "mensaje":"Se obtuvo el usuario",
        "id":id
    }

@app.get("/usuariosParam")
async def obtenerUsuarioParam(id:int):
     return{
            "mensaje":"Se obtuvo el usuario",
            "id":id
        }
     
@app.post("/usuarios",status_code=201)
async def crearUsuario(usuario:Usuario):
    global usuarios,idActual
    idActual = idActual+1
    usuario.id=idActual
    usuarios.append(usuario)
    return{
        "menaje":"Se creo el usuario",
        "data":usuario
    }
@app.get("/usuarios")
async def obtenerUsuarios():
    return{
        "mensaje":f"usuarios {len(usuarios)}",
        "data":usuarios
    }

@app.delete("/usuarios/{id}")
async def eliminarUsuario(id:int):
    for usuario in usuarios:
            if usuario.id == id:
                usuarios.remove(usuario)
                return{
                        "message":f"Usuario eliminado correctamente",
                    }
    return JSONResponse(
            status_code=404,
            content={
                "mensaje":f"No se encontro el usuario con el id {id}"
    }    )
