interface RankProps {
    rank: number
}

const getEmoji = (rank: number) => {
    switch (true) {
        case rank === 1.0:
            return "🌟"; // Highest rank
        case rank >= 0.8:
            return "⭐";
        case rank >= 0.6:
            return "✨";
        case rank >= 0.4:
            return "🌙";
        case rank >= 0.2:
            return "😕";
        case rank > 0.0:
            return "💧";
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