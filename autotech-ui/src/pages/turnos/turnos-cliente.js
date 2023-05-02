import Link from 'next/link';
import * as React from 'react';
import Button from '@mui/material/Button';
import Horarios from '../components/Horarios'

function Boton() {
    return (
        <div>
            <Button variant="contained">Volver</Button>
        </div>
    );
}

export default function Turno() {
    return (
        <>
            <h1>Sacar turno</h1>
            <h2>
                <Link href="/">Volver</Link>
            </h2>
            <Boton />
            <Horarios />
        </>
    );
}