function copiarAlPortapapeles(id_elemento) {
    console.log(id_elemento)
    navigator.clipboard.writeText('Hola mundo')

    if (id_elemento == 'email1') {
        navigator.clipboard.writeText('bielcostasamso@insalba.cat')

    }
    else if (id_elemento == 'email2') {
        navigator.clipboard.writeText('gbanoslopez@insalba.cat')

    }
    else if (id_elemento == 'email3') {
        navigator.clipboard.writeText('hmartinlozano@insalba.cat')

    }

    window.alert('Copiat! \n Ja pots enganxar el correu i contactarnos')
    
    window.open('https://mail.google.com/mail/?view=cm&amp;fs=1&amp;to=bielcostasmso%40insalba.cat&amp;authuser=0');
    
}