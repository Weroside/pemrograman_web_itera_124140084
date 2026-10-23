import PropTypes from "prop-types";
export function StatCard({ title, count }) {
  return (
    <article>
      <span>{title}</span>
      <strong>{count}</strong>
    </article>
  );
}
StatCard.propTypes = {
  title: PropTypes.string.isRequired,
  count: PropTypes.number.isRequired,
};
