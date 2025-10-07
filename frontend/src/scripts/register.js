document.getElementById('registerForm').addEventListener('submit', async (e) => {
  e.preventDefault();

  const username = document.getElementById('username').value;
  const email = document.getElementById('email').value;
  const password1 = document.getElementById('password1').value;
  const password2 = document.getElementById('password2').value;
  const nombre = document.getElementById('nombre').value;
  const apellido = document.getElementById('apellido').value;
  const telefono = document.getElementById('telefono').value;

  if (password1 !== password2) {
    alert('Las contraseñas no coinciden');
    return;
  }

  const data = {
    username,
    password: password1,
    email,
    profile: {
      nombre,
      apellido,
      telefono,
      role: 'admin'
    }
  };

  try {
    const response = await fetch('http://127.0.0.1:8000/auth/users/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });

    if (response.ok) {
      alert('Usuario registrado correctamente ✅');
      e.target.reset();
      window.location.href = '/login'; // opcional: redirige al login
    } else {
      const errorData = await response.json();
      console.error('Error:', errorData);
      alert('Error al registrar usuario ❌');
    }
  } catch (error) {
    console.error('Error en la conexión:', error);
    alert('Error en la conexión con el servidor ⚠️');
  }
});
