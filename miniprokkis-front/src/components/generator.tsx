import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';
import Slider from '@mui/material/Slider';

import "../styles/container.scss";
import { useState } from "react";
import { wordgenResponseSchema } from '../types/wordgen';

const Generator = () => {
    const [title, setTitle] = useState<string>("");
    const [chaos, setChaos] = useState<number>(3);
    const [disabled, setDisabled] = useState<boolean>(false);

    const getLastTwoWords = () => {
        const split = title.split(" ")
        if (split.length == 0) {
            return ""
        } else if (split.length == 1) {
            return split[0]
        } else {
            return split[split.length - 2] + " " + split[split.length - 1]
        }
    }

    const generate = async () => {
        const previous = getLastTwoWords()
        const response = await fetch(`http://127.0.0.1:5000/generate`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ previous: previous, chaos: previous == "" ? chaos * 9999 : chaos }),
        })
        try {
            const validated = await wordgenResponseSchema.validate(await response.json())
            console.log(validated.word)
            setTitle(title + " " + validated.word)
        } catch (e) {
            setDisabled(true)
        }
    }

    const deleteWord = () => {
        const split = title.split(" ")
        if (split.length > 1) {
            split.pop()
            setTitle(split.join(" "))
        }
        setDisabled(false)
    }

    return (
        <div className="container">
            <h1>title generator</h1>
            <Stack direction="row" spacing={2}>
                <Button variant="outlined" color="success" onClick={generate} disabled={disabled}>generate</Button>
                <Button variant="outlined" onClick={deleteWord} disabled={title.length == 0}>back</Button>
                <Button variant="outlined" color="error" onClick={() => { setTitle(""); setDisabled(false) }} disabled={title.length == 0}>clear</Button>
                <Button variant="outlined" onClick={() => navigator.clipboard.writeText(title)} >copy title</Button>
            </Stack>
            <h4>Randomness: {chaos}</h4>
            <Slider defaultValue={3} min={0} max={20} onChange={(e, v) => setChaos(v as number)} valueLabelDisplay="auto" />
            <h2>{title}</h2>
        </div>
    );
};

export default Generator;