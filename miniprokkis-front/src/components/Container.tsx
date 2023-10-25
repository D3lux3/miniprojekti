import TextField from "./TextField";
import "../styles/container.scss";
import Rank from "./Rank";
import { useState } from "react";

const Container = () => {
    const [rank, setRank] = useState<number>(0);
    return (
        <div className="container">
            <h1>youtube title ranker</h1>
            <TextField setRank={setRank} />
            <Rank rank={rank} />
        </div>
    );
};

export default Container;