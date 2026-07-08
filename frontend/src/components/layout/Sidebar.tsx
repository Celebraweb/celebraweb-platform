export default function Sidebar() {
  return (
    <aside
      style={{
        background: "#20232a",
        color: "#ffffff",
        width: "260px",
        minHeight: "100vh",
        display: "flex",
        flexDirection: "column",
        padding: "24px 20px",
        boxSizing: "border-box",
      }}
    >
      <div
        style={{
          marginBottom: "30px",
        }}
      >
        <h2
          style={{
            margin: 0,
            fontSize: "22px",
          }}
        >
          XOP Platform
        </h2>

        <p
          style={{
            marginTop: "6px",
            color: "#b8bcc4",
            fontSize: "13px",
          }}
        >
          CelebraWeb Platform
        </p>
      </div>

      <hr
        style={{
          borderColor: "#3b4048",
          marginBottom: "20px",
        }}
      />

      <MenuSection
        title="PLATFORM"
        items={[
          "🏠 Dashboard",
        ]}
      />

      <MenuSection
        title="ADMINISTRATION"
        items={[
          "🏢 Organizations",
          "👥 Users",
          "🛡 Roles",
        ]}
      />

      <MenuSection
        title="BUSINESS"
        items={[
          "📅 Events",
          "💌 Invitations",
          "💰 Finance",
          "📊 Analytics",
        ]}
      />

      <MenuSection
        title="PLATFORM SERVICES"
        items={[
          "⚙ Configuration",
          "🖥 Platform Administration",
          "🤖 Artificial Intelligence",
        ]}
      />

      <div
        style={{
          marginTop: "auto",
          paddingTop: "24px",
          fontSize: "12px",
          color: "#8d939b",
        }}
      >
        XOP Platform v0.2.0
      </div>
    </aside>
  );
}

type MenuSectionProps = {
  title: string;
  items: string[];
};

function MenuSection({
  title,
  items,
}: MenuSectionProps) {
  return (
    <div
      style={{
        marginBottom: "28px",
      }}
    >
      <div
        style={{
          fontSize: "11px",
          fontWeight: "bold",
          color: "#8d939b",
          marginBottom: "10px",
          letterSpacing: "1px",
        }}
      >
        {title}
      </div>

      {items.map((item) => (
        <div
          key={item}
          style={{
            padding: "8px 0",
            cursor: "pointer",
          }}
        >
          {item}
        </div>
      ))}
    </div>
  );
}