import TextField from "./TextField";
import "../styles/container.scss";

const Container = () => {

    return (
        <div className="container">
            <h1>Youtube Title Ranker</h1>
            <TextField />
            <p>Rank: 0.0</p>
        </div>
    );
};

export default Container;