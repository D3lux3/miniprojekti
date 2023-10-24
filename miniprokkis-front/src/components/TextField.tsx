import { TextField as TextF, styled } from "@mui/material";
import { useEffect, useState } from "react";

const StyledTextField = styled(TextF)({
    '& label.Mui-focused': {
        color: 'black',
    },
    '& .MuiInput-underline:after': {
        borderBottomColor: 'black',
    },
    '& .MuiOutlinedInput-root': {
        '&.Mui-focused fieldset': {
            borderColor: "black",
        },
        '& fieldset': {
            borderColor: 'black',
        },
        '&:hover fieldset': {
            borderColor: 'black',
        },

    },
});

const getRandomWord = () => {
    const randomWords = [
        "apple",
        "banana",
        "chocolate",
        "dog",
        "elephant",
        "flamingo",
        "giraffe",
        "hamburger",
        "iguana",
        "jazz",
        "koala",
        "lemon",
        "mango",
        "narwhal",
        "octopus",
        "penguin",
        "quokka",
        "rabbit",
        "strawberry",
        "tiger",
        "umbrella",
        "volcano",
        "watermelon",
        "xylophone",
        "yak",
        "zebra"
      ];
      return randomWords[Math.floor(Math.random()*randomWords.length)];
};

const TextField = () => {
    const [text, setText] = useState('');
    const [placeholdertext, setPlaceholdertext] = useState('');

    useEffect(() => {
        const delayReq = setTimeout(() => {
            setPlaceholdertext(`${text} ${getRandomWord()}`);
        }, 1000);
        return () => clearTimeout(delayReq);
    }, [text]);

    return (
        <StyledTextField onChange={(event) => setText(event.target.value)} placeholder={placeholdertext}/>
    );
};


export default TextField;