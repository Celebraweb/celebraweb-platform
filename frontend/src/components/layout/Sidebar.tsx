import { NavLink } from "react-router-dom";

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
          {
            label: "🏠 Dashboard",
            path: "/dashboard",
          },
        ]}
      />

      <MenuSection
        title="ADMINISTRATION"
        items={[
          {
            label: "🏢 Organizations",
            path: "/organizations",
          },
          {
            label: "👥 Users",
            path: "/users",
          },
          {
            label: "🛡 Roles",
            path: "/roles",
          },
        ]}
      />

      <MenuSection
        title="BUSINESS"
        items={[
          {
            label: "📅 Events",
            path: "#",
          },
          {
            label: "💌 Invitations",
            path: "#",
          },
          {
            label: "💰 Finance",
            path: "#",
          },
          {
            label: "📊 Analytics",
            path: "#",
          },
        ]}
      />

      <MenuSection
        title="PLATFORM SERVICES"
        items={[
          {
            label: "⚙ Configuration",
            path: "#",
          },
          {
            label: "🖥 Platform Administration",
            path: "#",
          },
          {
            label: "🤖 Artificial Intelligence",
            path: "#",
          },
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

interface MenuItem {
  label: string;
  path: string;
}

interface MenuSectionProps {
  title: string;
  items: MenuItem[];
}

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
        <NavLink
          key={item.label}
          to={item.path}
          style={({ isActive }) => ({
            display: "block",
            padding: "8px 0",
            color: isActive ? "#61dafb" : "#ffffff",
            textDecoration: "none",
            fontWeight: isActive ? "bold" : "normal",
          })}
        >
          {item.label}
        </NavLink>
      ))}
    </div>
  );
}