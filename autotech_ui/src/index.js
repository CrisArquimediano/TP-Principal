import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
// import App from './App';
// import { BrowserRouter } from 'react-router-dom';
import AsignaciosDeTecnicos from './pages/asignacion-de-tecnico/PanelDeAsignacion';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <AsignaciosDeTecnicos />
  </React.StrictMode>
);

