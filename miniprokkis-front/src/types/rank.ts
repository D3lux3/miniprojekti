import { object, number, InferType } from 'yup';


export const rankResponseSchema = object({
    rank: number().required().default(0)
}).required();


export type RankResponseType = InferType<typeof rankResponseSchema>;