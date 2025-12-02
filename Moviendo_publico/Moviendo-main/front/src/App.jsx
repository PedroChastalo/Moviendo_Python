import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import MainLayout from './components/MainLayout';
import Dashboard from './pages/Dashboard';
import Lists from './pages/Lista';
import Biblioteca from './pages/Biblioteca';
import Estatisticas from './pages/Estatisticas';
import './styles/global.css';

function App() {
  return (
    <Router>
      <Routes>
        <Route element={<MainLayout />}>
          <Route path="/" element={<Dashboard />} />
          <Route path="/biblioteca" element={<Biblioteca />} />
          <Route path="/listas" element={<Lists />} />
          <Route path="/estatisticas" element={<Estatisticas />} />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
