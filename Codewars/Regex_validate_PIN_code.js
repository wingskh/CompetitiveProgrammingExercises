// https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/javascript

function validatePIN(pin) {
  const pinList = [...pin].filter((pinChar => !isNaN(parseInt(pinChar)))).join('');
  return (pinList.length === 4 || pinList.length === 6) && pinList === pin;	
}

validatePIN("1"); // false
validatePIN("12"); // false 
validatePIN("123"); // false 
validatePIN("12345"); // false 
validatePIN("1234567"); // false 
validatePIN("-1234"); // false 
validatePIN("1.234"); // false
validatePIN("-1.234"); //false
validatePIN("00000000"); // false
validatePIN("a234"); // false
validatePIN(".234"); // false
validatePIN("1234"); // true
validatePIN("0000"); // true
validatePIN("1111"); // true
validatePIN("123456"); // true
validatePIN("098765"); // true
validatePIN("000000"); // true
validatePIN("123456"); // true
validatePIN("090909"); // true
