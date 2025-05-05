package com.brightvoltelectric.utils;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DatabaseConnection {
    private static final String URL = "jdbc:mysql://localhost:3306/brightvolt";
    private static final String USER = "your_mysql_user";
    private static final String PASSWORD = "your_mysql_password";

    public static Connection initializeDatabase() throws SQLException, ClassNotFoundException {
        // Load MySQL JDBC Driver
        Class.forName("com.mysql.cj.jdbc.Driver");

        // Establish and return the connection
        return DriverManager.getConnection(URL, USER, PASSWORD);
    }
}
