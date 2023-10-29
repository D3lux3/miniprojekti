interface RankProps {
    rank: number
}

const getEmoji = (rank: number) => {
    switch (true) {
        case rank >= 9.0:
            return "🌟"; // Highest rank
        case rank >= 0.7:
            return "⭐";
        case rank >= 0.5:
            return "✨";
        case rank >= 0.3:
            return "🌙";
        case rank >= 0.1:
            return "😕";
        case rank > -0.1:
            return "💧";
        case rank > -0.3:
            return "🌧️";
        case rank > -0.5:
            return "⛈️️";
        case rank > -0.7:
            return "🌪️";
        default:
            return "❌"; // Lowest rank
    }
};

const Rank = ({ rank }: RankProps) => {

    return (
        <>
            <p>rank: <strong>{rank}</strong> {getEmoji(rank)}</p>
        </>
    );
};


export default Rank;