import { TextField as TextF, styled } from '@mui/material'
import { Dispatch, useEffect, useState } from 'react'
import { rankResponseSchema } from '../types/rank'

interface TextFieldProps {
  setRank: Dispatch<number>
}

const StyledTextField = styled(TextF)({
  '& label.Mui-focused': {
    color: 'black',
  },
  '& .MuiInput-underline:after': {
    borderBottomColor: 'black',
  },
  '& .MuiOutlinedInput-root': {
    '&.Mui-focused fieldset': {
      borderColor: 'black',
    },
    '& fieldset': {
      borderColor: 'black',
    },
    '&:hover fieldset': {
      borderColor: 'black',
    },
  },
})

const TextField = ({ setRank }: TextFieldProps) => {
  const [text, setText] = useState<string>('')

  useEffect(() => {
    if (text.length > 0) {
      const delayReq = setTimeout(async () => {
        const getRank = async () => {
          const response = await fetch(`http://127.0.0.1:5000/rank`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: text }),
          })
          const validated = await rankResponseSchema.validate(
            await response.json()
          )
          return validated.rank
        }
        setRank(await getRank())
      }, 250)
      return () => clearTimeout(delayReq)
    }
    setRank(0)
    return
  }, [text])

  return (
    <StyledTextField
      onChange={(event) => setText(event.target.value)}
      placeholder={'Enter your title'}
    />
  )
}

export default TextField
