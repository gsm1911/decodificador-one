<%-- 
    Document   : validaInserirChamada
    Created on : 23 de mai. de 2024, 13:25:51
    Author     : mathe
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@page import="carmenacademia.model.bean.Chamada"%>
<%@page import="carmenacademia.controller.ControllerChamada"%>

<!DOCTYPE html>

<%
    String A = request.getParameter("IDMATRICULA");
    int idMatricula = Integer.parseInt(A);
    int idAluno = Integer.parseInt(request.getParameter("IDALUNO"));
    String presente = request.getParameter("PRESENTE");
    boolean presentee = Boolean.getBoolean(presente);
    String endereco = request.getParameter("DATADACHAMADA");
    String a = "";

    Chamada sis = new Chamada(idMatricula, idAluno, presentee, endereco, a);
    ControllerChamada siscont = new ControllerChamada();
    siscont.inserir(sis);
    // REDIRECIONA PARA A PAG LOGIN.JSP
    String url = "inserirChamada.jsp";
    response.sendRedirect(url);
%>
