<%-- 
    Document   : alterarChamada
    Created on : 23 de mai. de 2024, 13:55:01
    Author     : mathe
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@page import="carmenacademia.model.bean.Chamada"%>
<%@page import="carmenacademia.controller.ControllerChamada"%>

<%
    String cod = request.getParameter("CODIGODAMATRICULA");
    int codigoDamatricula = Integer.parseInt(cod);
    Chamada sis = new Chamada(codigoDamatricula);
    ControllerChamada sisCont = new ControllerChamada();
    sis = sisCont.buscar(sis);
    String pbusca = request.getParameter("PBUSCA");

%>

<html>
    <%@include file="../../inc/materalizeWeb.inc" %>
    <title>ALTERAR - CHAMADA</title>
    <body>
       <body>
    <div class="container">
        <h1 class="center-align">ALTERAR CHAMADA</h1>
        <form name="alterarChamada" action="validaAlterarChamada.jsp" method="post">
            <div class="row">
                <div class="input-field col s12">
                    <input type="text" id="idMatricula" name="IdMatricula" value="<%=sis.getIdMatricula()%>">
                    <label for="idMatricula">ID da Matricula</label>
                </div>
            </div>
            <div class="row">
                <div class="input-field col s12">
                    <input type="text" id="presente" name="Presente" value="<%=sis.isPresente()%>">
                    <label for="presente">Presente</label>
                </div>
            </div>
            <div class="row">
                <div class="input-field col s12">
                    <input type="text" id="data" name="Data" value="<%=sis.getData()%>">
                    <label for="data">Data da Chamada</label>
                </div>
            </div>
            <input type="hidden" name="IdChamada" value="<%=sis.getIdChamada()%>">
            <input type="hidden" name="PBUSCA" value="<%=pbusca%>">
            <div class="row">
                <div class="col s12">
                    <button type="submit" class="btn waves-effect waves-light">OK</button>
                    <a href="javascript:history.go(-1);" class="btn waves-effect waves-light red right">Cancelar</a>
                </div>
            </div>
        </form>
    </div>
</body>
</html>
