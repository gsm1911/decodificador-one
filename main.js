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
    let entrada = String(document.getElementById('entrada_texto').value);
    let saida0 = entrada.replace("enter", "e");
    let saida1 = saida0.replace("imes", "i");
    let saida2 = saida1.replace("ai", "a");
    let saida3 = saida2.replace("ober", "o");
    let saida4 = saida3.replace("ufat", "u");
    for(let i = 0; i<9; i++){
        saida0 = saida4.replace("enter", "e");
        saida1 = saida0.replace("imes", "i");
        saida2 = saida1.replace("ai", "a");
        saida3 = saida2.replace("ober", "o");
        saida4 = saida3.replace("ufat", "u");
    }

    document.getElementById("saida_texto").value = saida4;
}