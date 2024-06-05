<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@page import="carmenacademia.model.bean.Turma"%>
<%@page import="carmenacademia.controller.ControllerTurma"%>

<%
    String idturmaa = request.getParameter("IdTurma");
    int idturma = Integer.parseInt(idturmaa);
    String instrutor = request.getParameter("Instrutor");
    int instrutorr = Integer.parseInt(instrutor);
    String horario = request.getParameter("horario");
    String dataInicio = request.getParameter("dataInicio");
    String dataFim = request.getParameter("dataFim");
    String atividade = request.getParameter("atividade");
   

    Turma sis = new Turma(idturma,instrutorr , horario, dataInicio, dataFim, atividade);
    ControllerTurma siscont = new ControllerTurma();
    siscont.alterar(sis);
    String pbusca = request.getParameter("PBUSCA");
    // REDIRECIONA PARA A PAG LOGIN.JSP
    String url = "validaConsultarTurma.jsp?NOME=" + pbusca;
    response.sendRedirect(url);
%>