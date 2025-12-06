import "./main.scss";
import "@popperjs/core";
import PerfectScrollbar from "perfect-scrollbar";
import SmoothScrollbar from "smooth-scrollbar";


import "./js/material-dashboard";

import DataTable from 'datatables.net';
import 'datatables.net-dt/css/dataTables.dataTables.css';
import "bootstrap/dist/css/bootstrap.min.css";


document.querySelectorAll(".datatable").forEach((el)=>{
    new DataTable(el);
});