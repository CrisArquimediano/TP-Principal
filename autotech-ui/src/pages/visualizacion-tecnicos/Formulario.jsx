import { useState, useEffect } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSearch } from '@fortawesome/free-solid-svg-icons';
import Typography from '@mui/material/Typography'
import { Input, Box, Button } from '@mui/material';
import MenuItem from "@mui/material/MenuItem";
import FormControl from "@mui/material/FormControl";
import Select from "@mui/material/Select";
import axios from 'axios';
import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';
import KeyboardArrowUpIcon from '@mui/icons-material/KeyboardArrowUp';
import IconButton from '@mui/material/IconButton';
import Collapse from '@mui/material/Collapse';

const Formulario = () => {

    const [listaTecnicos, setTecnicos] = useState([]);
    const [tablaTecnicos, setTablaTecnicos] = useState([]);
    const [expanded, setExpanded] = React.useState(false);
    const [detalleTrabajos, setDetalleTrabajos] = useState([]);
    const [mostrarInfo, setMostrarInfo] = useState(false);

    const [valoresBusqueda, setValoresBusqueda] = useState({
        nombre: "",
        dni: "",
        categoria: "",

    });

    let endPoint = `https://autotech.onrender.com/busquedatecnicos/filtro/?`

    /*  const traerTecnicos = () => {
        return axios.get(`${endPoint}${
        ""
            }`)
            .then(response=>{
          setTecnicos(response.data);
                setTablaTecnicos(response.data);
        }).catch(error=>{
          console.log(error);
        })
      }
    */

    const filtrarTecnicos = () => {

        return axios.get(`${endPoint}${(!(valoresBusqueda.nombre.length <= 0)) &&
                (!(valoresBusqueda.dni.length <= 0)) &&
                (!(valoresBusqueda.categoria.length <= 0)) ?
                `nombre_completo=${valoresBusqueda.nombre}&dni=${valoresBusqueda.dni}&categoria=${valoresBusqueda.categoria}&` :

                (!(valoresBusqueda.nombre.length <= 0)) && (!(valoresBusqueda.dni.length <= 0)) ?
                    `nombre_completo=${valoresBusqueda.nombre}&dni=${valoresBusqueda.dni}` :
                    (!(valoresBusqueda.nombre.length <= 0)) && (!(valoresBusqueda.categoria.length <= 0)) ?
                        `nombre_completo=${valoresBusqueda.nombre}&categoria=${valoresBusqueda.categoria}&` :
                        (!(valoresBusqueda.dni.length <= 0)) && (!(valoresBusqueda.categoria.length <= 0)) ?
                            `dni=${valoresBusqueda.dni}&categoria=${valoresBusqueda.categoria}` :

                            !(valoresBusqueda.nombre.length <= 0) ? `nombre_completo=${valoresBusqueda.nombre}&` :
                                !(valoresBusqueda.dni.length <= 0) ? `dni=${valoresBusqueda.dni}` :
                                    !(valoresBusqueda.categoria.length <= 0) ? `categoria=${valoresBusqueda.categoria}&` :
                                        ""
            }`)
            .then(response => {
                setTecnicos(response.data);
                setTablaTecnicos(response.data);

                if (mostrarInfo) {
                    setMostrarInfo(!mostrarInfo);
                }

            }).catch(error => {
                console.log(error);
            })
    };

    const handleChange = (event) => {
        const { name, value } = event.target;
        setValoresBusqueda((prevState) => ({
            ...prevState,
            [name]: value,
        }));
        console.log(valoresBusqueda.nombre);
    };

    let endPointDetalle = `https://autotech.onrender.com/busquedatecnicos/tecnico`
    const mostrarDetalle = (id) => (event) => {
        let ruta = `${endPointDetalle}${`/${id}/`}`
        return axios.get(ruta)
            .then(response => {
                setDetalleTrabajos(response.data);
                setMostrarInfo(!mostrarInfo);
            }).catch(error => {
                console.log(error);
            })
    };


    useEffect(() => {
        filtrarTecnicos();
    }, [])

    return (
        <Box className="background-color">
            <Typography variant="h1">Tecnicos</Typography>
            <Box className="row d-flex justify-content-center">
                <Box className="col-12 col-md-8 col-lg-6 col-xl-6">
                    <Box className="card shadow-2-strong" sx={{ borderRadius: "1rem" }}>
                        <Box className="card-body p-5 text-center row" >
                            <Typography variant="6">Búsqueda:</Typography>

                            <Input type="search" name="nombre" value={valoresBusqueda.nombre} onChange={handleChange} placeholder="Buscar por Nombre" className="form-control form-control-lg mb-2"></Input>
                            <Input type="search" name="dni" value={valoresBusqueda.dni} onChange={handleChange} placeholder="Buscar por DNI" className="form-control form-control-lg mb-2"></Input>

                            <FormControl sx={{ ml: 1 }}>
                                <Typography variant="6">Categoría</Typography>
                                <Select
                                    value={valoresBusqueda.categoria}
                                    onChange={handleChange}
                                    sx={{ height: 30 }}
                                    name="categoria"
                                >
                                    <MenuItem value=""><em>None</em></MenuItem>
                                    <MenuItem value={"A"}>A</MenuItem>
                                    <MenuItem value={"B"}>B</MenuItem>
                                    <MenuItem value={"C"}>C</MenuItem>
                                    <MenuItem value={"D"}>D</MenuItem>
                                </Select>
                            </FormControl>

                            <Box className="m-2">
                                <Button variant="contained" color="secondary" onClick={filtrarTecnicos}>
                                    Buscar<FontAwesomeIcon icon={faSearch} />
                                </Button>
                            </Box>
                        </Box>
                    </Box>
                </Box>
            </Box>

            <TableContainer component={Paper} className="mt-5">
                <Table sx={{ minWidth: 650 }} aria-label="simple table">

                    <TableHead>
                        <TableRow>
                            <TableCell align="center">ID</TableCell>
                            <TableCell align="center">Nombre completo</TableCell>
                            <TableCell align="center">DNI</TableCell>
                            <TableCell align="center">Categoria</TableCell>
                            <TableCell align="center">Taller</TableCell>
                            <TableCell align="center">Trabajos realizados</TableCell>
                        </TableRow>
                    </TableHead>

                    <TableBody>

                        {listaTecnicos.tecnicos && listaTecnicos.tecnicos.map((tecnicoObj) => (
                            <TableRow
                                key={tecnicoObj.id_empleado}
                                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                            >
                                <TableCell align="center">{tecnicoObj.id_empleado}</TableCell>
                                <TableCell align="center">{tecnicoObj.nombre_completo}</TableCell>
                                <TableCell align="center">{tecnicoObj.dni}</TableCell>
                                <TableCell align="center">{tecnicoObj.categoria}</TableCell>
                                <TableCell align="center">{tecnicoObj.branch}</TableCell>
                                <TableCell align="center">
                                    <IconButton
                                        aria-label="expand row"
                                        size="small"
                                        onClick={mostrarDetalle(tecnicoObj.id_empleado)}
                                    >
                                        {mostrarInfo ? <KeyboardArrowUpIcon /> : <KeyboardArrowDownIcon />}
                                    </IconButton>
                                </TableCell>
                            </TableRow>
                        ))}

                        <TableRow>
                            <TableCell style={{ paddingBottom: 0, paddingTop: 0 }} colSpan={6}>
                                <Collapse in={mostrarInfo} timeout="auto" unmountOnExit>
                                    <Box sx={{ margin: 1 }}>
                                        <Typography variant="h6" gutterBottom component="div">
                                            Detalle
                                        </Typography>

                                        <Table size="small" aria-label="purchases">
                                            <TableHead>
                                                <TableRow>
                                                    <TableCell align="center">Patente</TableCell>
                                                    <TableCell align="center">Fecha inicio</TableCell>
                                                    <TableCell align="center">Hora inicio</TableCell>
                                                    <TableCell align="center">Fecha fin</TableCell>
                                                    <TableCell align="center">Hora fin</TableCell>
                                                    <TableCell align="center">Tipo</TableCell>
                                                </TableRow>
                                            </TableHead>
                                            <TableBody>
                                                {detalleTrabajos.map((detalle, index) => (
                                                    <TableRow key={index}>
                                                        <TableCell component="th" scope="row">{detalle.patente}</TableCell>
                                                        <TableCell>{detalle.fecha_inicio}</TableCell>
                                                        <TableCell align="center">{detalle.hora_inicio}</TableCell>
                                                        <TableCell align="center">{detalle.fecha_fin}</TableCell>
                                                        <TableCell align="center">{detalle.hora_fin}</TableCell>
                                                        <TableCell align="center">{detalle.tipo}</TableCell>
                                                    </TableRow>
                                                ))}
                                            </TableBody>
                                        </Table>
                                    </Box>
                                </Collapse>
                            </TableCell>
                        </TableRow>
                    </TableBody>
                </Table>
            </TableContainer>
        </Box>
    );
}

export default Formulario;