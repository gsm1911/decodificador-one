var pat = /^[a-z\s]+$/;

function criptografar(){
    let entrada = String(document.getElementById('entrada_texto').value);
    
    if(pat.test(entrada) == true){
        entrada = entrada.replaceAll("e", "enter");
        entrada = entrada.replaceAll("i", "imes");
        entrada = entrada.replaceAll("a", "ai");
        entrada = entrada.replaceAll("o", "ober");
        entrada = entrada.replaceAll("u", "ufat");
        document.getElementById("saida_texto").value = entrada
    }
    else{
        document.getElementById("saida_texto").value = "Insira somente letras minusculas e sem acento."
    }
}

function descriptografar(){
    let entrada = document.getElementById("entrada_texto").value

    entrada = entrada.replaceAll("enter", "e");
    entrada = entrada.replaceAll("imes", "i");
    entrada = entrada.replaceAll("ai", "a");
    entrada = entrada.replaceAll("ober", "o");
    entrada = entrada.replaceAll("ufat", "u");

    console.log(entrada);
    document.getElementById("saida_texto").value = entrada;
}
