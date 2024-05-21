id_send.onclick = (e) => {
    if (id_login.value.replaceAll(' ', '') === ''){
        e.preventDefault()
        alert('!alert! Не заполнен логин')
        }
    else if (id_password1.value.replaceAll(' ', '') === ''){
        e.preventDefault()
        alert('!alert! Не заполнен пароль')
        }
    else if (id_password2.value.replaceAll(' ', '') === ''){
        e.preventDefault()
        alert('!alert! Не заполнен пароль')
        }
    else if (id_phone.value.replaceAll(' ', '') === ''){
        e.preventDefault()
        alert('!alert! Не заполнен телефон')
        }
    else if (id_password0.value !== id_password1.value) {
        e.preventDefault()
        alert('!alert! Пароли не совпадают')
        }
}
