<%-- 
    Document   : validaAlterarChamada
    Created on : 23 de mai. de 2024, 13:55:42
    Author     : mathe
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@page import="carmenacademia.model.bean.Chamada"%>
<%@page import="carmenacademia.controller.ControllerChamada"%>

<%
    String cod = request.getParameter("IdChamada");
    int IdChamada = Integer.parseInt(cod);
    int IdMatricula = Integer.parseInt(request.getParameter("IdMatricula"));
    
    String presentee = request.getParameter("Presente");
    boolean presente = Boolean.parseBoolean(presentee);
    String data = request.getParameter("Data");
    
    Chamada sis = new Chamada(IdChamada, IdMatricula, presente, data);
    ControllerChamada siscont = new ControllerChamada();
    siscont.alterar(sis);
    String pbusca = request.getParameter("PBUSCA");
    // REDIRECIONA PARA A PAG LOGIN.JSP
    String url = "validaConsultarChamada.jsp?NOME=" + pbusca;
    response.sendRedirect(url);
%>
