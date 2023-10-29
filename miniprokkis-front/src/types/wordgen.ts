import { object, string, InferType } from 'yup';


export const wordgenResponseSchema = object({
    word: string().required().default("")
}).required();


export type WordgenResponseType = InferType<typeof wordgenResponseSchema>;