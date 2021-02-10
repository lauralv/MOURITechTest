
function palindrome(str) {

    str = str.replace(/\W/g, '').toLowerCase();
    
    const reversed = str.split('').reverse().join('');

    return str === reversed;
}

