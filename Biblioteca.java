class Libro {
    String titulo;
    String autor;
    boolean disponible = true;

    Libro(String titulo, String autor) {
        this.titulo = titulo;
        this.autor = autor;
    }

    String prestar() {
        if (disponible) {
            disponible = false;
            return "El libro '" + titulo + "' ha sido prestado.";
        }
        return "El libro '" + titulo + "' no está disponible.";
    }

    String devolver() {
        disponible = true;
        return "El libro '" + titulo + "' ha sido devuelto.";
    }
}

class Usuario {
    String nombre;
    String idUsuario;

    Usuario(String nombre, String idUsuario) {
        this.nombre = nombre;
        this.idUsuario = idUsuario;
    }

    String solicitarLibro(Libro libro) {
        return libro.prestar();
    }

    String devolverLibro(Libro libro) {
        return libro.devolver();
    }
}

public class Biblioteca {
    public static void main(String[] args) {
        Libro libro1 = new Libro("El coronel no tiene quien le escriba", "Gabriel García Marquez");
        System.out.println(libro1.prestar());
    }
}
    
