// Função para alternar entre o campo de mês e ano
function toggleFields() {
    var tipo = document.querySelector('input[name="tipo"]:checked');

    // Verifica se algum botão de radio foi selecionado
    if (tipo) {
        tipo = tipo.value;

        if (tipo === "entrada") {
            // Se "Mensal" for selecionado, exibe o campo de mês e esconde o campo de ano
            document.getElementById('mesField').style.display = 'block';
            document.getElementById('anoField').style.display = 'none';
        } else {
            // Se "Anual" for selecionado, exibe o campo de ano e esconde o campo de mês
            document.getElementById('mesField').style.display = 'none';
            document.getElementById('anoField').style.display = 'block';
        }
    }
}

// Inicializa os eventos quando o modal é aberto
$(document).ready(function () {
    // Abertura do Modal 1
    $('#exampleModal').on('show.bs.modal', function () {
        toggleFields(); // Chama a função para garantir que o campo correto seja exibido

        // Adiciona evento de mudança nos radio buttons para chamar a função toggleFields
        $('input[name="tipo"]').on('change', toggleFields);
    });

    // Abertura do Modal 2 (se necessário)
    $('#Modal2').on('show.bs.modal', function () {
        // Lógica específica para o Modal 2, se houver
    });

    // Abertura do Modal 3 (se necessário)
    $('#Modal3').on('show.bs.modal', function () {
        // Lógica específica para o Modal 3, se houver
    });
});
