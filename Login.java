package login;

import java.util.Scanner;

public class Login {
    public static void main(String[] args) {
        String pass = "Mqr1520";
        String user = "Mdln";
        String usuario, password;
        
        Scanner teclado = new Scanner(System.in);
        
        System.out.print("Proporciona usuario: ");
        usuario = teclado.nextLine();
        
        System.out.print("Proporciona password: ");
        password = teclado.nextLine();
        
        if (password.equals(pass) && usuario.equals(user)) {
            System.out.println("Bienvenido(a): " + usuario);
        } else {
            System.out.println("Usuario y/o contrasena invalidos.");
        }
        
        teclado.close();
    }
}

