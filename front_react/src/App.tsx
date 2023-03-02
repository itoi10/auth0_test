import './App.css';
import LoginButton from './login';
import Profile from './profile';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <LoginButton/>
        <Profile/>
      </header>
    </div>
  );
}

export default App;
