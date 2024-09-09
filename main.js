var pat = /^[a-z\s]+$/;

function criptografar(){
    let entrada = String(document.getElementById('entrada_texto').value);
    let saida = [];
    if(pat.test(entrada) == true){
        for(let i = 0; i<entrada.length; i++){
            if(entrada[i] == 'e'){
                saida[i] = 'enter';
            }
            else if(entrada[i] == 'i'){
                saida[i] = 'imes';
            }
            else if(entrada[i] == 'a'){
                saida[i] = 'ai';
            }
            else if(entrada[i] == 'o'){
                saida[i] = 'ober';
            }
            else if(entrada[i] == 'u'){
                saida[i] = 'ufat';
            }
            else{
                saida[i] = entrada[i];
            }
        }
    
        document.getElementById("saida_texto").value = saida.join("");
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
