package com.brightvoltelectric;

import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class ContactFormServlet extends HttpServlet {

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        // Read form fields
        String name = request.getParameter("name");
        String email = request.getParameter("email");
        String message = request.getParameter("message");

        // For demo purposes, we just print to console or log
        System.out.println("New contact request:");
        System.out.println("Name: " + name);
        System.out.println("Email: " + email);
        System.out.println("Message: " + message);

        // Set response content type
        response.setContentType("text/html");

        // Send a simple thank-you page
        PrintWriter out = response.getWriter();
        out.println("<html><body>");
        out.println("<h2>Thank you for contacting BrightVolt Electric!</h2>");
        out.println("<p>We have received your message and will get back to you shortly.</p>");
        out.println("<a href='index.html'>Return to Home</a>");
        out.println("</body></html>");
    }
}
