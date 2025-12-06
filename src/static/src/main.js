import "./main.scss";
import "@popperjs/core";
import PerfectScrollbar from "perfect-scrollbar";
import SmoothScrollbar from "smooth-scrollbar";


import "./js/material-dashboard";
import TomSelect from "tom-select";
import 'tom-select/dist/css/tom-select.css';
import "bootstrap/dist/css/bootstrap.min.css";

import { TabulatorFull as Tabulator } from "tabulator-tables";
import "tabulator-tables/dist/css/tabulator.min.css";


window.addEventListener("load", () => {
    document.querySelectorAll(".datatable").forEach((el) => {

        const columns = JSON.parse(el.dataset.columns);

        new Tabulator(el, {
            layout: "fitColumns",
            columns: columns,
            
            headerFilterPlaceholder: "Pesquisar...",

            // 🔢 Paginação
            pagination: "local",
            paginationSize: 10,
            paginationSizeSelector: [5, 10, 25, 50],

            // Mensagem quando não houver registros
            placeholder: "Nenhum registro encontrado",

            // Carregar da tabela HTML
            tableBuilt: function () {
            },

            // Permite renderizar HTML corretamente no campo "actions"
            rowFormatter: function(row){
                // força Tabulator a manter HTML do <td>
            },
        });
    });
});



document.querySelectorAll('.select-multiple').forEach(function(el) {
    new TomSelect(el, {
        plugins: ['remove_button'],
        placeholder: "Selecione ...",
        hideSelected: true,
        closeAfterSelect: false,
        maxItems: null,
    });
})