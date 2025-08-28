class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return f"'{self.titulo}' prestado."
        return f"'{self.titulo}' no disponible."

    def devolver(self):
        self.disponible = True
        return f"'{self.titulo}' devuelto."

class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre

    def solicitar_libro(self, libro):
        return libro.prestar()

    def devolver_libro(self, libro):
        return libro.devolver()


# HERENCIA
class UsuarioPremium(Usuario):
    def __init__(self, id_usuario, nombre, nivel):
        super().__init__(id_usuario, nombre)
        self.nivel = nivel
        
# POLIMORFISMO
    def solicitar_libro(self, libro): 
        return f"[Premium {self.nivel}] " + super().solicitar_libro(libro)


# EJEMPLO
libro = Libro("El coronel no tiene quien le escriba", "Gabriel Garcia Marquez")
u1 = Usuario(101, "Juan")
u2 = UsuarioPremium(102, "Ana", "Oro")

print(u1.solicitar_libro(libro))
print(u2.solicitar_libro(libro))
print(u1.devolver_libro(libro))
